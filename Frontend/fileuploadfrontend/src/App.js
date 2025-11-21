import React, { useState } from "react";
import './App.css';

function App() {
  const [name, setName] = useState("");
  const [file, setFile] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!file) {
      alert("Please upload a file");
      return;
    }

    console.log("Name:", name);
    console.log("File:", file);
    // TODO: Upload to S3

    alert("uploaded file successfully");
  };

  return (
    <div className="app-container">
      <div className="card">
        <h1 className="title">File Uploader Service</h1>

        <form onSubmit={handleSubmit} className="form">
          <div>
            <label className="label">Name</label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="input"
              placeholder="Enter your name"
            />
          </div>

          <div>
            <label className="label">Upload File</label>
            <input
              type="file"
              onChange={(e) => setFile(e.target.files[0])}
              className="input"
            />
          </div>

          <button type="submit" className="submit-btn">Submit</button>
        </form>
      </div>
    </div>
  );
}

export default App;