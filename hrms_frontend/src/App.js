// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Use Routes instead of Switch
import StaffOnboarding from './components/StaffOnboarding';
import StaffList from './components/StaffList';
import StaffDetail from './components/StaffDetail';
import TopMenu from './components/TopMenu';
import './App.css';

const App = () => {
  return (
    <Router>
      <div>
        <TopMenu />
        <Routes>
          <Route path="/" element={<StaffOnboarding />} /> 
          <Route path="/staff-list" element={<StaffList />} /> 
          <Route path="/staff/:id" element={<StaffDetail />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
