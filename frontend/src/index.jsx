import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const messages = [
  {
    id: 1,
    from: "sender@example.com",
    subject: "Hello World",
    date: "2025-02-01",
    snippet: "This is a short snippet of the email...",
    body: "This is the full content of the email.",
    spam_alert: false,
  },
  {
    id: 2,
    from: "spam@example.com",
    subject: "Win a prize!",
    date: "2025-02-01",
    snippet: "You have won a lucky draw!",
    body: "Click the link to claim your prize.",
    spam_alert: true,
  },
];

const EmailItem = ({ message }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className={`email ${message.spam_alert ? "spam" : ""} mb-3 p-3 border rounded`}> 
      <div className="email-header p-2 bg-light border-bottom position-relative">
        <p><strong>From:</strong> {message.from}</p>
        <p><strong>Subject:</strong> {message.subject}</p>
        <p><strong>Date:</strong> {message.date}</p>
        <p><strong>Snippet:</strong> {message.snippet}</p>
        <button className="btn btn-primary" onClick={() => setIsOpen(!isOpen)}>
          {isOpen ? "Hide Email" : "View Email"}
        </button>
        <span className="spam-indicator position-absolute top-0 end-0 p-2 fw-bold">
          {message.spam_alert ? "Spam" : "Not Spam"}
        </span>
      </div>
      {isOpen && (
        <div className="email-body p-2">
          <p><strong>Body:</strong></p>
          <p>{message.body}</p>
        </div>
      )}
    </div>
  );
};

const GmailInbox = () => {
  return (
    <div className="container mt-4">
      <h1>Your Gmail Inbox</h1>
      {messages.map((msg) => (
        <EmailItem key={msg.id} message={msg} />
      ))}
    </div>
  );
};

export default GmailInbox;
