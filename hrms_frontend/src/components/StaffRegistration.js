import React, { useState } from 'react';
import axiosInstance from '../axiosInstance';  // Import the Axios instance
import ErrorMessage from '../components/ErrorMessage';  // Import the ErrorMessage component
import StaffDetail from '../components/StaffDetail';  // Import the StaffDetail component

const StaffRegistration = ({ mobileNumber, verifiedOtp }) => {
  const [surname, setSurname] = useState('');
  const [otherName, setOtherName] = useState('');
  const [dateOfBirth, setDateOfBirth] = useState('');
  const [idPhoto, setIdPhoto] = useState(null);
  const [errorMessage, setErrorMessage] = useState('');  // State for error message
  const [registeredUser, setRegisteredUser] = useState(null); // State for the registered user

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('surname', surname);
    formData.append('other_name', otherName);
    formData.append('date_of_birth', dateOfBirth);
    formData.append('mobile_number', mobileNumber);
    formData.append('otp', verifiedOtp);  // Append verified OTP
    if (idPhoto) {
      formData.append('id_photo', idPhoto);
    }

    try {
      // Make the API call to register the staff
      const response = await axiosInstance.post('/accounts/staff/', formData);
      setRegisteredUser(response.data); // Store the registered user's details
      setErrorMessage('');  // Clear any previous errors on success
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
      {registeredUser ? (
        // Render the StaffDetail component if user is registered
        <StaffDetail user={registeredUser} />
      ) : (
        <>
          <h2>Register Staff</h2>

          {/* Display error message if any */}
          <ErrorMessage message={errorMessage} />

          <form onSubmit={handleSubmit}>
            <div>
              <input
                type="text"
                placeholder="Surname"
                value={surname}
                onChange={(e) => setSurname(e.target.value)}
                required
              />
            </div>
            <div>
              <input
                type="text"
                placeholder="Other Name"
                value={otherName}
                onChange={(e) => setOtherName(e.target.value)}
                required
              />
            </div>
            <div>
              <input
                type="date"
                value={dateOfBirth}
                onChange={(e) => setDateOfBirth(e.target.value)}
                required
              />
            </div>
            <div>
              <input
                type="file"
                onChange={(e) => setIdPhoto(e.target.files[0])}
                required
              />
            </div>
            <div>
              <button type="submit">Register Staff</button>
            </div>
          </form>
        </>
      )}
    </div>
  );
};

export default StaffRegistration;
