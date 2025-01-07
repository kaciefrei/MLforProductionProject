import React, { useState } from "react";

function App() {
  const [formData, setFormData] = useState({
    Temperature: "",
    RH: "",
    Ws: "",
    Rain: "",
    FFMC: "",
    DMC: "",
    DC: "",
    ISI: "",
    BUI: "",
    FWI: "",
  });

  const [result, setResult] = useState(null);

  // Fonction pour gérer les changements dans les champs du formulaire
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Fonction de soumission du formulaire
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("https://forest-fire-backend-production.up.railway.app/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      setResult({
        risk_level: data.prediction === 1 ? "High Risk" : "Low Risk",
        prediction_value: data.prediction,
      });
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Forest Fire Risk Prediction</h1>
      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map((key) => (
          <div key={key} style={{ marginBottom: "10px" }}>
            <label>
              {key}:
              <input
                type="number"
                name={key}
                value={formData[key]}
                onChange={handleChange}
                style={{ marginLeft: "10px" }}
                required
              />
            </label>
          </div>
        ))}
        <button type="submit" style={{ padding: "10px 20px", cursor: "pointer" }}>
          Predict
        </button>
      </form>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h2>Prediction Result</h2>
          <p>Risk Level: <b>{result.risk_level}</b></p>
          <p>Prediction Value: {result.prediction_value}</p>
        </div>
      )}
    </div>
  );
}

export default App;
// test