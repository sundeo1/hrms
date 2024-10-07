import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom'; 
import axiosInstance from '../axiosInstance';  
import ErrorMessage from '../components/ErrorMessage'; 

const StaffList = () => {
  const [staffList, setStaffList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState('');

  const fetchStaffList = async () => {
    try {
      const response = await axiosInstance.get('/accounts/staff/');
      setStaffList(response.data.results); 
    } catch (error) {
      setErrorMessage('Error fetching staff list');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStaffList();
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h2>Staff List</h2>
      <ErrorMessage message={errorMessage} />

      {staffList.length === 0 ? (
        <p>No staff members found.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Employee Number</th>
              <th>Surname</th>
              <th>Other Name</th>
              <th>Date of Birth</th>
              <th>ID Photo</th>
              <th>Actions</th> 
            </tr>
          </thead>
          <tbody>
            {staffList.map((staff) => (
              <tr key={staff.id}>
                <td>{staff.staff_id}</td>
                <td>{staff.surname}</td>
                <td>{staff.other_name}</td>
                <td>{staff.date_of_birth}</td>
                <td>
                  {staff.id_photo ? (
                    <img src={staff.id_photo} alt={`${staff.surname} ${staff.other_name}`} style={{ width: '30px', height: 'auto' }} />
                  ) : (
                    'No Photo'
                  )}
                </td>
                <td>
                  <Link to={`/staff/${staff.id}`}>View</Link> 
                  {' | '}
                  <Link to={`/staff/${staff.id}/edit`}>Edit</Link> 
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default StaffList;
