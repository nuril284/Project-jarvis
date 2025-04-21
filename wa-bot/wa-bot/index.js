const { default: makeWASocket, DisconnectReason, fetchLatestBaileysVersion, useMultiFileAuthState } = require("@whiskeysockets/baileys");
const { Boom } = require("@hapi/boom");
const fs = require("fs");

async function startSock() {
    const { state, saveCreds } = await useMultiFileAuthState("./auth_info");
    const { version, isLatest } = await fetchLatestBaileysVersion();

    const sock = makeWASocket({
        version,
        auth: state,
        printQRInTerminal: true
    });

    sock.ev.on("creds.update", saveCreds);

    sock.ev.on("connection.update", (update) => {
        const { connection, lastDisconnect } = update;
        const shouldReconnect = lastDisconnect?.error?.output?.statusCode !== DisconnectReason.loggedOut;

        if (connection === "close") {
            console.log("connection closed due to", lastDisconnect?.error, ", reconnecting:", shouldReconnect);
            if (shouldReconnect) startSock();
        } else if (connection === "open") {
            console.log("WA connection opened");
        }
    });

    sock.ev.on("messages.upsert", (m) => {
        console.log("msg: ", JSON.stringify(m, null, 2));
    });
}

startSock();
