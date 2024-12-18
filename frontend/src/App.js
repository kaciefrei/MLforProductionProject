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

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      setResult(data);
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