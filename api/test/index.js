const fs = require('fs');

const API_URL = "http://localhost:8023/predecir";
const METRICAS = [
  "piña", // test_01.jpg
  "frutilla" // test_01.jpg
]

async function query(fileName) {
  return new Promise(async (resolve, reject) => {
    try {
      let PATH = `${__dirname}\\images\\${fileName}`;

      const formData = new FormData();
      formData.append("image", PATH);

      const options = {
        method: "POST",
        body: formData,
      }

      const response = await fetch(API_URL, options)
        .then((response) => response.json())
        .catch((err) => {
          throw err;
        })

      return resolve(response);
    } catch (err) {
      return resolve({ fruta: "error" })
    }
  })
}

async function main() {
  try {
    console.log("[🐛] Iniciando pruebas ...")

    // Construye las consultas utilizando las imagenes del directorio.
    let querys = [];
    fs.readdirSync(`${__dirname}\\images`).forEach((file) => {
      querys.push(query(file));
    });

    // Ejecutan las consultas.
    await Promise.all(querys)
      .then((response) => {
        let index = 0;
        response.forEach((res) => {
          let resultado = res.fruta === METRICAS[index] ? "[✅] OK" : "[❌] ERROR";
          console.log(`[TEST: ${index + 1}] `, resultado, res.fruta);

          index++;
        })
      })
      .catch((err) => {
        throw err;
      })

  } catch (err) {
    // console.log("[❌] ERROR al realizar las pruebas.")
  }
}

main()
