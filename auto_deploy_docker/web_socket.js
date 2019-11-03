// References:
// 1. https://developer.mozilla.org/en-US/docs/Web/API/WebSocket

// Create WebSocket connection.
const socket = new WebSocket("ws://45.146.122.60:6789")

// Connection Opened
socket.addEventListener('open', (event) => {
    msg = {msg: 'hello, websocket'};
    socket.send(JSON.stringify(msg))});

// Listen for messages
socket.addEventListener('message', (event) => {
    console.log('Message from server ', event.data);
});


