async function send() {
  const input = document.getElementById("input");
  const chat = document.getElementById("chat");

  const message = input.value;

  const res = await fetch("http://localhost:8000/api/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      user_id: "user1",
      message: message
    })
  });

  const data = await res.json();

  chat.innerHTML += `<p><b>You:</b> ${message}</p>`;
  chat.innerHTML += `<p><b>AI:</b> ${data.response}</p>`;

  input.value = "";
}