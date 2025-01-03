import React, { useState } from "react";
import axios from "axios";
import { FaPaperclip, FaPaperPlane } from "react-icons/fa"; 
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState("");

  const handleSendMessage = async () => {
    if (!message && !file) {
      setResponse("Please provide a message or upload a file.");
      return;
    }

    const formData = new FormData();
    if (message) formData.append("message", message);
    if (file) formData.append("file", file);

    try {
      const res = await axios.post("http://127.0.0.1:5000/generate", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResponse(res.data.response);
    } catch (error) {
      console.error("Error fetching response:", error);
      setResponse("An error occurred while processing your request.");
    }
  };

  return (
    <div className="app-container">
      <div className="message-box">
        <h1 className="header-text">What can I help with?</h1>
        <div className="input-section">
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Enter a message"
            className="input-field"
          />
          <label htmlFor="file-upload" className="file-upload-label">
            <FaPaperclip className="attach-icon" /> Attach File
          </label>
          <input
            id="file-upload"
            type="file"
            onChange={(e) => setFile(e.target.files[0])}
            className="file-input"
          />
          {file && <p className="file-name">Selected File: {file.name}</p>}
        </div>
        <button onClick={handleSendMessage} className="send-button">
          <FaPaperPlane className="send-icon" /> Send
        </button>
        <p className="response-text">Response: {response}</p>
      </div>
    </div>
  );
}

export default App;
