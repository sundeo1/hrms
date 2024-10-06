import React, { useState } from 'react';
import axiosInstance from '../axiosInstance';
import ErrorMessage from '../components/ErrorMessage';

const OtpVerification = ({ setStep, mobileNumber, setVerifiedOtp }) => {
  const [otp, setOtp] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const handleOtpVerification = async () => {
    try {
      await axiosInstance.post('/accounts/users/verify-otp/', { mobile_number: mobileNumber, otp });
      
      // Save the verified OTP and proceed to the next step
      setVerifiedOtp(otp);  // Save the verified OTP for the registration step
      setStep(3);           // Move to staff registration step
    } catch (error) {
      // Extract the actual error message(s) from the API response
      const errorResponse = error.response?.data;
      if (errorResponse) {
        // Combine all error messages if there are multiple fields with errors
        const errorMessages = Object.values(errorResponse).flat();  
        setErrorMessage(errorMessages.join(', ')); // Join multiple error messages with a comma
      } else {
        setErrorMessage('An unknown error occurred, please try again.');
      }
    }
  };

  return (
    <div>
      
      <h4>Enter the verification code received to proceed</h4>

      {/* Use the reusable ErrorMessage component */}
      <ErrorMessage message={errorMessage} />

      <input
        type="text"
        placeholder="Enter OTP"
        value={otp}
        onChange={(e) => setOtp(e.target.value)}
      />
      <button onClick={handleOtpVerification}>Verify Code</button>
    </div>
  );
};

export default OtpVerification;
