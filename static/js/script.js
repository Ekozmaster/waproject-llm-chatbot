document.getElementById("start-new-chat").addEventListener("click", function () {
    setTimeout(function () {
        document.getElementById("main-page").style.display = "none";
        document.getElementById("chat-window").style.display = "flex";
    }, 500);
    document.getElementById("main-page").classList.add("main-page-fadeout");
    document.getElementById("chat-window").classList.remove("chat-window-fadeout");
});

document.getElementById("back-to-main").addEventListener("click", function () {
    setTimeout(function () {
        document.getElementById("chat-window").style.display = "none";
        document.getElementById("main-page").style.display = "flex";
    }, 500);
    document.getElementById("main-page").classList.remove("main-page-fadeout");
    document.getElementById("chat-window").classList.add("chat-window-fadeout");
});



let chatMessages = [];  // [{ sender: 'human' or 'ai', content: 'message content' }, ...]

const RefreshChatMessages = () => {
    const chatMessagesParent = document.getElementById('chat-messages-parent');
    if (chatMessages.length === 0) {
        chatMessagesParent.style.display = 'none';
        return;
    }
    chatMessagesParent.style.display = 'flex';

    const chatMessagesContainer = document.getElementById('chat-messages-container');
    chatMessagesContainer.innerHTML = '';
    const converter = new showdown.Converter();
    chatMessages.forEach(message => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(message.sender);
        messageDiv.innerHTML = converter.makeHtml(message.content);
        chatMessagesContainer.appendChild(messageDiv);
    });
    document.getElementById('chat-messages').scrollTop = chatMessagesContainer.scrollHeight;
    document.getElementById('ask-something').style.display = 'none';
};

document.addEventListener('DOMContentLoaded', async function() {
    chatMessages = [];

    const response = await fetch('/langchain-messages/');
    if (!response.ok) {
        throw new Error('Failed to retrieve chat history');
    }
    const data = await response.json();
    chatMessages = data.messages;
    RefreshChatMessages();
});



// Chat form submission
const form = document.getElementById('chat-form');
form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const messageInput = form.message;

    try {
        chatMessages.push({ sender: 'human', content: messageInput.value });
        messageInput.value = '';
        RefreshChatMessages();
        const response = await fetch('/send-message/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ messages: chatMessages }),
        });
        if (!response.ok) {
            throw new Error('Failed to send message');
        }
        const messagesResponse = await response.json();
        chatMessages = messagesResponse.messages;
        RefreshChatMessages();

    } catch (error) {
        console.error('Error:', error.message);
        alert('Failed to send the message. Please try again.');
    }
});



// Delete chat history button
document.getElementById('delete-chat-history').addEventListener('click', async () => {
    const confirmed = confirm('Are you sure you want to delete the chat history?');
    if (confirmed) {
        const response = await fetch('/delete-langchain-messages/', {
            method: 'DELETE'
        });
        if(!response.ok) {
            throw new Error('Failed to delete chat history');
        }
        const data = await response.json();
        chatMessages = data.messages;
        RefreshChatMessages();
        document.getElementById('ask-something').style.display = 'flex';
    }
});
