import React, { useState } from 'react';
import axios from 'axios';

const SignIn = () => {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/api/v1/token/', formData);
            const { access } = response.data; // Assuming the token is under 'access' key

            // Store the JWT token in local storage
            localStorage.setItem('token', access);

            console.log(response.data); // Handle successful sign-in
            alert('Sign in successful!');
            // You can also redirect the user to another page here if needed
        } catch (error) {
            console.error('Error during sign-in:', error);
            alert('Sign in failed. Please check your credentials.');
        }
    };

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', maxWidth: '300px', margin: '0 auto' }}>
                <h2>Sign In</h2>
                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    onChange={handleChange}
                    required
                    style={{ marginBottom: '10px', width: '100%' }}
                />
                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    onChange={handleChange}
                    required
                    style={{ marginBottom: '10px', width: '100%' }}
                />
                <button type="submit" style={{ width: '100%', marginTop: '10px' }}>Sign In</button>
            </form>
        </div>
    );
};

export default SignIn;
