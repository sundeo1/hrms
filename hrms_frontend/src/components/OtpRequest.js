import React, { useState } from 'react';
import axiosInstance from '../axiosInstance';
import ErrorMessage from '../components/ErrorMessage';

const OtpRequest = ({ setStep, setMobileNumber }) => {
  const [mobileNumber, setNumber] = useState('');
  const [errorMessage, setErrorMessage] = useState('');  // Add error state

  const handleOtpRequest = async () => {
    try {
      await axiosInstance.post('/accounts/users/request-otp/', { mobile_number: mobileNumber });
      setMobileNumber(mobileNumber);
      setStep(2);  // Move to OTP verification step
    } catch (error) {
      // Extract the actual error message(s) from the API response
      const errorResponse = error.response?.data;
      if (errorResponse) {
        // Combine all error messages if there are multiple fields with errors
        const errorMessages = Object.values(errorResponse).flat();  
        setErrorMessage(errorMessages);
      } else {
        setErrorMessage('An unknown error occurred, please try again.');
      }
    }
  };

  return (
    <div>
      <h3>Register New Staff</h3>
      <h4>Enter mobile number to receive verification code on your phone</h4>

      {/* Use the reusable ErrorMessage component */}
      <ErrorMessage message={errorMessage} />

      <input
        type="text"
        placeholder="Enter mobile number"
        value={mobileNumber}
        onChange={(e) => setNumber(e.target.value)}
      />
      <button onClick={handleOtpRequest}>Request Verification Code</button>
    </div>
  );
};

export default OtpRequest;
