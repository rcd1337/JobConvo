import { signup } from '@/actions/auth'
import { useRouter } from 'next/router'
import styles from '@/styles/Forms.module.css'
import React, { useState } from 'react'

export function SignupForm({onClick}) {
  const router = useRouter()
  const [isApplicant, setIsApplicant] = useState(true);
  return (
    <div>
    <form action={signup} className={styles.fields}>
      <div>
        <label htmlFor="name">Name</label>
        <input id="name" name="name" placeholder="Name" />
      </div>
      <div>
        <label htmlFor="email">Email</label>
        <input id="email" name="email" type="email" placeholder="Email" />
      </div>
      <div>
        <label htmlFor="password">Password</label>
        <input id="password" name="password" type="password" />
      </div>
      <div className={styles.radio}>
          <label htmlFor="account_type">Account type</label>
          <input type="radio" id="Recruiter" name="account_type" value="Recruiter" onClick={() => setIsApplicant(false)}/>
          <label htmlFor="Recruiter">Recruiter</label>
          <input type="radio" id="Applicant" name="account_type" value="Applicant" onClick={() => setIsApplicant(true)}/>
          <label htmlFor="Applicant">Applicant</label>
      </div>
      {isApplicant ? 
          <>
            <label htmlFor="experience">Experience</label>
            <input id="experience" name="experience" placeholder="Experience" />
            <label htmlFor="Education">Education</label>
            <select name="education" id="education">
              <option value="elementary">Elementary</option>
              <option value="high_school">Highschool</option>
              <option value="technologist">Technologist</option>
              <option value="bachelors">Bachelors</option>
              <option value="postgraduate">Post graduate</option>
              <option value="doctorate">Doctorate</option>
            </select>
            <label htmlFor="salary">Salary range</label>
            <select name="salary" id="salary">
              <option value="up_to_1000">Up to $1000</option>
              <option value="from_1001_to_2000">Between $1001 and $2000</option>
              <option value="from_2001_to_3000">Between $2001 and $3000</option>
              <option value="above_3000">Above $3000</option>
            </select>
          </>
          : 
          <>
            <label htmlFor="company">Company name</label>
            <input id="company" name="company" placeholder="Company Name" />
          </>
      }
      <div className={styles.buttons}>
        <button className={styles.button} type="submit" onClick={() => router.push('/')}>Sign Up</button>
        <button className={styles.button}  type="button" onClick={onClick}>Sign In</button>
      </div>
    </form>
    </div>
  )
}