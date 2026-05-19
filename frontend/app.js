import axios from "axios";
import { useState } from "react";

function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState("");
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const login = async () => {
    const res = await axios.post("http://localhost:8000/auth/login", null, {
      params: { email, password },
    });
    setToken(res.data.access_token);
  };

  const sendMessage = async () => {
    const res = await axios.post(
      "http://localhost:8000/api/chat",
      { message },
      {
        headers: { Authorization: `Bearer ${token}` },
      }
    );
    setResponse(res.data.response);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>AI Dashboard</h1>

      <h3>Login</h3>
      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      <button onClick={login}>Login</button>

      <h3>Chat</h3>
      <input
        placeholder="Ask..."
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={sendMessage}>Send</button>

      <p><b>Response:</b> {response}</p>
    </div>
  );
}

export default App;