import React from 'react';
import { Link } from 'react-router-dom';

const MainPage = () => {
    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>JobConvo fron-end</h1>
            <Link to="/signin">
                <button style={{ margin: '10px', padding: '10px 20px' }}>Sign In</button>
            </Link>
            <Link to="/signup">
                <button style={{ margin: '10px', padding: '10px 20px' }}>Sign Up</button>
            </Link>
        </div>
    );
};

export default MainPage;
