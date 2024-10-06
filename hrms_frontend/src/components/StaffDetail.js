import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axiosInstance from '../axiosInstance';  // Import the Axios instance
import ErrorMessage from '../components/ErrorMessage'; // Import the ErrorMessage component

const StaffDetail = () => {
  const { id } = useParams();
  const [staff, setStaff] = useState(null);
  const [errorMessage, setErrorMessage] = useState(''); // State for error message
  const [loading, setLoading] = useState(true); // Loading state

  const fetchStaffDetail = async () => {
    try {
      const response = await axiosInstance.get(`/accounts/staff/${id}/`);
      setStaff(response.data);
    } catch (error) {
      // Extract the error message
      const errorResponse = error.response?.data;
      if (errorResponse) {
        const errorMessages = Object.values(errorResponse).flat();  
        setErrorMessage(errorMessages.join(', ')); // Join error messages into a single string
      } else {
        setErrorMessage('Error fetching staff details');
      }
    } finally {
      setLoading(false); // Set loading to false regardless of success or failure
    }
  };

  useEffect(() => {
    fetchStaffDetail();
  }, [id]);

  if (loading) return <div>Loading...</div>; // Display loading text while fetching data

  return (
    <div>
      <h2>Staff Details</h2>
      
      {/* Display error message if any */}
      <ErrorMessage message={errorMessage} />
      
      {errorMessage ? ( // Check for error messages first
        <p>{errorMessage}</p>
      ) : (
        staff ? (
          <>
            <p><strong>Staff ID:</strong> {staff.staff_id}</p>
            <p><strong>Surname:</strong> {staff.surname}</p>
            <p><strong>Other Name:</strong> {staff.other_name}</p>
            <p><strong>Date of Birth:</strong> {staff.date_of_birth}</p>
            {staff.id_photo && (
              <div>
                <strong>ID Photo:</strong>
                <img src={staff.id_photo} alt="ID Photo" style={{ maxWidth: '200px', marginTop: '10px' }} />
              </div>
            )}
          </>
        ) : (
          <p>No staff details found.</p>
        )
      )}
    </div>
  );
};

export default StaffDetail;
