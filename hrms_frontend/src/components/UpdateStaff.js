import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axiosInstance from '../axiosInstance';  
import ErrorMessage from '../components/ErrorMessage';  

const UpdateStaff = () => {
  const { id } = useParams();
  const navigate = useNavigate(); 
  const [dateOfBirth, setDateOfBirth] = useState('');
  const [idPhoto, setIdPhoto] = useState(null);
  const [mobileNumber, setMobileNumber] = useState('');  
  const [errorMessage, setErrorMessage] = useState('');
  const [loading, setLoading] = useState(true);

  // Fetch current staff details
  useEffect(() => {
    const fetchStaffDetail = async () => {
      try {
        const response = await axiosInstance.get(`/accounts/staff/${id}/`);
        setDateOfBirth(response.data.date_of_birth);
        setMobileNumber(response.data.mobile_number);  
      } catch (error) {
        setErrorMessage('Error fetching staff details');
      } finally {
        setLoading(false);
      }
    };

    fetchStaffDetail();
  }, [id]);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('date_of_birth', dateOfBirth);
    formData.append('mobile_number', mobileNumber);  

    if (idPhoto) {
      formData.append('id_photo', idPhoto);
    }

    try {
      await axiosInstance.patch(`/accounts/staff/${id}/`, formData);
      alert('Staff updated successfully');
      navigate(`/staff/${id}`);  
    } catch (error) {
      setErrorMessage('Error updating staff details');
    }
  };

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h2>Update Staff</h2>
      <ErrorMessage message={errorMessage} />

      <form onSubmit={handleSubmit}>
        <div>
          <label>Date of Birth:</label>
          <input
            type="date"
            value={dateOfBirth}
            onChange={(e) => setDateOfBirth(e.target.value)}
            required
          />
        </div>
        <div>
          <label>ID Photo:</label>
          <input
            type="file"
            onChange={(e) => setIdPhoto(e.target.files[0])}
          />
        </div>
        <button type="submit">Update Staff</button>
      </form>
    </div>
  );
};

export default UpdateStaff;
