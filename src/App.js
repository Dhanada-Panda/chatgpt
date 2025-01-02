import React, { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const handleSendMessage = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:5000/generate", { message });
      setResponse(res.data.response);
    } catch (error) {
      console.error("Error fetching response:", error);
      setResponse("An error occurred.");
    }
  };

  return (
    <div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Enter a message"
      />
      <button onClick={handleSendMessage}>Send</button>
      <p>Response: {response}</p>
    </div>
  );
}

export default App;
