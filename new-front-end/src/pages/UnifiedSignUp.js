// src/pages/UnifiedSignUp.js
import React, { useState } from 'react';
import axios from 'axios';
import { SALARY_RANGE_EXPECTATION, EDUCATIONAL_LEVEL } from '../constants';

const UnifiedSignUp = () => {
  const [formType, setFormType] = useState('applicant');
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    experience: '',
    salaryRangeExpectation: '',
    educationalLevel: '',
    companyName: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleFormTypeChange = (e) => {
    setFormType(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data =
      formType === 'applicant'
        ? {
            account_data: {
              email: formData.email,
              password: formData.password,
            },
            applicant_profile_data: {
              experience: formData.experience,
              educational_level: formData.educationalLevel,
              salary_range_expectation: formData.salaryRangeExpectation,
            },
          }
        : {
            account_data: {
              email: formData.email,
              password: formData.password,
            },
            recruiter_profile_data: {
              company_name: formData.companyName,
            },
          };

    const endpoint =
      formType === 'applicant'
        ? 'http://localhost:8000/api/v1/register-applicant/'
        : 'http://localhost:8000/api/v1/register-recruiter/';

    try {
      const response = await axios.post(endpoint, data);
      alert('Registration successful!');
      console.log('Registration successful:', response.data);
    } catch (error) {
      alert('Registration failed. Please try again.');
      console.error('Error during registration:', error);
    }
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '10px', width: '300px' }}>
        <h2>Sign Up</h2>
        
        <label>
          Select Account Type:
          <select value={formType} onChange={handleFormTypeChange}>
            <option value="applicant">Applicant</option>
            <option value="recruiter">Recruiter</option>
          </select>
        </label>

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
        />

        {formType === 'applicant' && (
          <>
            <input
              type="text"
              name="experience"
              placeholder="Experience"
              value={formData.experience}
              onChange={handleChange}
            />
            <select
              name="salaryRangeExpectation"
              value={formData.salaryRangeExpectation}
              onChange={handleChange}
            >
              <option value="">Select Salary Range</option>
              {Object.values(SALARY_RANGE_EXPECTATION).map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
            <select
              name="educationalLevel"
              value={formData.educationalLevel}
              onChange={handleChange}
            >
              <option value="">Select Educational Level</option>
              {Object.values(EDUCATIONAL_LEVEL).map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
          </>
        )}

        {formType === 'recruiter' && (
          <input
            type="text"
            name="companyName"
            placeholder="Company Name"
            value={formData.companyName}
            onChange={handleChange}
          />
        )}

        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
};

export default UnifiedSignUp;
