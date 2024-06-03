document.addEventListener("DOMContentLoaded", function() {
    const chatForm = document.getElementById("chat-form");
    const chatMessages = document.getElementById("chat-messages");
    const sendButton = document.querySelector("button[type='submit']");  // Select the send button

    // Initially, the chatbot is not responding, so enable the send button
    let isChatbotResponding = false;
    enableSendButton();

    chatForm.addEventListener("submit", async function(e) {
        e.preventDefault();
        const userMessage = document.getElementById("user-input").value;

        // Display user message
        displayMessage("user", userMessage);

        // Disable the send button while the chatbot is responding
        disableSendButton();

        // Send user message to the server
        try {
            const response = await fetch("/chat", {
                method: "POST",
                body: new URLSearchParams({ user_input: userMessage }),
                headers: { "Content-Type": "application/x-www-form-urlencoded" }
            });
            if (!response.ok) {
                throw new Error(`Request failed with status ${response.status}`);
            }

            const data = await response.json();
            const botResponse = data.response;
            displayMessage("bot", botResponse);
        } catch (error) {
            console.error(error);
            // Handle error appropriately
        } finally {
            // Re-enable the send button when the chatbot has responded
            enableSendButton();
        }

        // Clear user input
        document.getElementById("user-input").value = "";
    });

    function displayMessage(sender, message) {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message", sender);
        messageElement.innerText = message;
        chatMessages.appendChild(messageElement);

        // Scroll to the bottom of the chat
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function enableSendButton() {
        isChatbotResponding = false;
        sendButton.removeAttribute("disabled");
    }

    function disableSendButton() {
        isChatbotResponding = true;
        sendButton.setAttribute("disabled", "true");
    }
});
