import React from 'react';

const ErrorMessage = ({ message }) => {
  if (!message) return null;

  return (
    <div style={{ color: 'white', backgroundColor: 'red', padding: '10px', marginBottom: '10px', borderRadius: '4px' }}>
      {/* Check if the message is an array or single string and render accordingly */}
      {Array.isArray(message) ? (
        <ul>
          {message.map((msg, index) => (
            <li key={index}>{msg}</li>
          ))}
        </ul>
      ) : (
        <p>{message}</p>
      )}
    </div>
  );
};

export default ErrorMessage;
