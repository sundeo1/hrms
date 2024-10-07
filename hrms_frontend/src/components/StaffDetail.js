import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axiosInstance from '../axiosInstance';  
import ErrorMessage from '../components/ErrorMessage'; 

const StaffDetail = () => {
  const { id } = useParams();
  const [staff, setStaff] = useState(null);
  const [errorMessage, setErrorMessage] = useState(''); 
  const [loading, setLoading] = useState(true); 

  const fetchStaffDetail = async () => {
    try {
      const response = await axiosInstance.get(`/accounts/staff/${id}/`);
      setStaff(response.data);
    } catch (error) {
      // Extract the error message
      const errorResponse = error.response?.data;
      if (errorResponse) {
        const errorMessages = Object.values(errorResponse).flat();  
        setErrorMessage(errorMessages.join(', ')); 
      } else {
        setErrorMessage('Error fetching staff details');
      }
    } finally {
      setLoading(false); 
    }
  };

  useEffect(() => {
    fetchStaffDetail();
  }, [id]);

  if (loading) return <div>Loading...</div>; 

  return (
    <div>
      <h2>Staff Details</h2>
      
      
      <ErrorMessage message={errorMessage} />
      
      {errorMessage ? ( 
        <p>{errorMessage}</p>
      ) : (
        staff ? (
          <>
            <p><strong>Employee Number:</strong> {staff.staff_id}</p>
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
