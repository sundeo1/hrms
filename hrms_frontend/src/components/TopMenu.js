// src/components/TopMenu.js

import React from 'react';
import { Link } from 'react-router-dom';

const TopMenu = () => {
  return (
    
    <nav>
        <h1>Human Resource Management System</h1>
      <ul>
        <li>
          <Link to="/">Register New Staff</Link>
        </li>
        <li>
          <Link to="/staff-list">View Staff List</Link>
        </li>
      </ul>
    </nav>
  );
};

export default TopMenu;
