const https = require("https");
const fs = require("fs");
const path = require("path");

const CONFIG_PATH = path.join(__dirname, "..", "dashboard", "prospector-config.json");
let config = {};
try {
  config = JSON.parse(fs.readFileSync(CONFIG_PATH, "utf-8"));
} catch (e) {
  console.error("Erro ao ler prospector-config.json:", e.message);
}

const COOLIFY = config.coolify || {
  url: "https://coolify.dluz.com.br",
  apiUrl: "https://coolify.dluz.com.br/api/v1",
  token: "9|ZFyMfXFPUEKhZG2d6eF8RNHO9f0bVdbawJMLfa3M9c32706c",
  projectId: "a96qaj5yukctlrnk31ynhoso",
  projectName: "Clientes Sites",
  environment: "production",
  environmentUuid: "cr8m0qzzynl254n2z2evaxvn",
  serverUuid: "y39qmwncbniv5ux9fd7cs2wt",
  destinationUuid: "vac5t6k8m8ibrurv9d94iyf9"
};

function request(endpoint, method = "GET", payload = null) {
  return new Promise((resolve, reject) => {
    const data = payload ? JSON.stringify(payload) : null;
    const url = new URL(`${COOLIFY.apiUrl}/${endpoint}`);
    
    const req = https.request(url, {
      method: method,
      headers: {
        "Authorization": `Bearer ${COOLIFY.token}`,
        "Content-Type": "application/json",
        "Accept": "application/json",
        ...(data ? { "Content-Length": Buffer.byteLength(data) } : {})
      }
    }, (res) => {
      let body = "";
      res.on("data", chunk => body += chunk);
      res.on("end", () => {
        try {
          resolve({ status: res.statusCode, data: JSON.parse(body || "{}") });
        } catch {
          resolve({ status: res.statusCode, data: body });
        }
      });
    });

    req.on("error", reject);
    if (data) req.write(data);
    req.end();
  });
}

function parseArgs() {
  const args = process.argv.slice(2);
  const params = {};
  for (let i = 0; i < args.length; i++) {
    if (args[i].startsWith("--")) {
      const key = args[i].substring(2);
      const val = args[i + 1] && !args[i + 1].startsWith("--") ? args[i + 1] : true;
      params[key] = val;
    }
  }
  return params;
}

async function main() {
  const args = parseArgs();
  const action = args.action || "list";

  console.log(`\n☁️  COOLIFY DEPLOY — PROJETO CLIENTES (${COOLIFY.projectName} / ${COOLIFY.projectId})`);
  console.log(`Ambiente: ${COOLIFY.environment} (${COOLIFY.environmentUuid})\n`);

  switch (action) {
    case "list": {
      const res = await request(`projects/${COOLIFY.projectId}/${COOLIFY.environment}`);
      const apps = res.data.applications || [];
      console.log(`=== SITES DE CLIENTES NO COOLIFY (Total: ${apps.length}) ===`);
      apps.forEach(a => {
        console.log(`\n• [${a.uuid}] ${a.name}`);
        console.log(`  Status:    ${a.status}`);
        console.log(`  Domínio:   ${a.fqdn || "(sem domínio)"}`);
        console.log(`  Git Repo:  ${a.git_repository || "N/A"} (${a.git_branch || "main"})`);
      });
      break;
    }

    case "deploy": {
      const uuid = args.uuid;
      if (!uuid) {
        console.error("❌ Erro: Informe --uuid <APP_UUID>");
        return;
      }
      console.log(`🚀 Disparando deploy para o app ${uuid}...`);
      const res = await request(`deploy?uuid=${uuid}`, "POST");
      console.log("Resposta do deploy:");
      console.log(JSON.stringify(res.data, null, 2));
      break;
    }

    case "status": {
      const uuid = args.uuid;
      if (!uuid) {
        console.error("❌ Erro: Informe --uuid <DEPLOYMENT_UUID>");
        return;
      }
      const res = await request(`deployments/${uuid}`);
      console.log("Status:", res.data.status);
      console.log(JSON.stringify(res.data, null, 2));
      break;
    }

    case "restart": {
      const uuid = args.uuid;
      if (!uuid) {
        console.error("❌ Erro: Informe --uuid <APP_UUID>");
        return;
      }
      console.log(`🔄 Reiniciando container ${uuid}...`);
      const res = await request(`applications/${uuid}/restart`, "POST");
      console.log(JSON.stringify(res.data, null, 2));
      break;
    }

    default:
      console.log(`Ação: ${action}`);
      console.log("Uso: node deploy-coolify.js --action [list | deploy | status | restart] [--uuid <UUID>]");
  }
}

main().catch(console.error);
