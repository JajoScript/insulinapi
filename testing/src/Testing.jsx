import { useState } from "react";

function Testing(props) {
  // 1. Manejo del estado.
  const [file, setFile] = useState(null);

  // 2. Ciclo de vida.
  // 3. Metodos.
  const handleFile = (e) => {
    const file = e.target.files[0];

    if (file) {
      setFile(file);
    }
  };

  const sendFile = async () => {
    const formData = new FormData();
    formData.append("image", file);

    await fetch("http://127.0.0.1:8023/predecir", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => console.log(data));
  };

  // 4. Renderizado.
  return (
    <div className="container">
      <div className="content">
        <h1 className="title">InsulinAPI testing</h1>
        <p className="subtitle">Prueba de comunicación de imagenes</p>

        <input
          type="file"
          name="file"
          className="inputFile"
          id="inputFile"
          onChange={(e) => handleFile(e)}
        />

        <button className="button" onClick={() => sendFile()}>
          Enviar
        </button>
      </div>
    </div>
  );
}

// Exportación 🐶.
export default Testing;
