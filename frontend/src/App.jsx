import { useState } from "react";
import ReactMarkdown from "react-markdown";

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [socket, setSocket] = useState(null);

  async function askAI() {
    setResponse("");

    const ws = new WebSocket("ws://127.0.0.1:8000/ws");

    setSocket(ws);

    ws.onopen = () => {
      ws.send(question);
    };

    ws.onmessage = (event) => {
      setResponse((prev) => prev + event.data);
    };

    ws.onclose = () => {
      console.log("WebSocket closed");
    };

    ws.onerror = (error) => {
      console.error("WebSocket Error:", error);
    };
  }

  function stopAI() {
    if (socket) {
      socket.send("__STOP__");
    }
  }

  return (
    <div
      style={{
        minHeight: "100vh",
        backgroundColor: "#071330",
        color: "white",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        paddingTop: "30px",
      }}
    >
      <h1
        style={{
          fontSize: "64px",
          marginBottom: "20px",
        }}
      >
        JarvisOS 🚀
      </h1>

      <div
        style={{
          display: "flex",
          gap: "10px",
          marginBottom: "25px",
        }}
      >
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask something..."
          style={{
            width: "500px",
            padding: "12px",
            fontSize: "16px",
          }}
        />

        <button
          onClick={askAI}
          style={{
            padding: "12px 20px",
            cursor: "pointer",
          }}
        >
          Ask AI
        </button>

        <button
          onClick={stopAI}
          style={{
            padding: "12px 20px",
            cursor: "pointer",
          }}
        >
          Stop
        </button>
      </div>

      <div
        style={{
          width: "90%",
          maxWidth: "1000px",
          minHeight: "250px",
          border: "1px solid #334155",
          borderRadius: "12px",
          padding: "25px",
          backgroundColor: "#081633",
          textAlign: "left",
          overflowWrap: "break-word",
          boxSizing: "border-box",
        }}
      >
        <h2
          style={{
            textAlign: "center",
            marginBottom: "25px",
          }}
        >
          Response
        </h2>

        <ReactMarkdown>
          {response}
        </ReactMarkdown>
      </div>
    </div>
  );
}

export default App;