// src/Navbar.js

import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

const Navbar = () => {
    const navigate = useNavigate();

    const handleLogOff = () => {
        // Clear the token from localStorage
        localStorage.removeItem('token');

        // Show success alert
        alert('You have been logged off successfully!');

        // Redirect to the homepage
        navigate('/');
    };

    return (
        <nav style={{ display: 'flex', justifyContent: 'center', padding: '10px', background: '#f2f2f2' }}>
            <Link to="/" style={{ textDecoration: 'none', color: 'blue', margin: '0 15px' }}>Home</Link>
            <Link to="/job-listings" style={{ textDecoration: 'none', color: 'blue', margin: '0 15px' }}>Job Listings</Link>
            <Link to="/job-listings/create" style={{ textDecoration: 'none', color: 'blue', margin: '0 15px' }}>Create Job Listing</Link>
            <Link to="/report" style={{ textDecoration: 'none', color: 'blue', margin: '0 15px' }}>Report</Link>
            <button 
                onClick={handleLogOff} 
                style={{ 
                    marginLeft: '15px', 
                    cursor: 'pointer', 
                    background: 'transparent', 
                    color: 'blue', 
                    border: 'none', 
                    padding: '0', 
                    font: 'inherit', 
                }}
            >
                Log Off
            </button>
        </nav>
    );
};

export default Navbar;
