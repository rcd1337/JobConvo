
import {SignupForm} from "@/ui/signup-form";
import {SignInForm} from "@/ui/signin-form";
import {Navbar} from "@/ui/navbar";
import React, { useState } from 'react'
import styles from '@/styles/Forms.module.css'
import { useRouter } from 'next/router'

export default function Home() {
  const [login, setlogin] = useState(true);
  const router = useRouter()

  return (
    <>
      <Navbar/>
      <div className={styles.login}>
      <h1>login</h1>
      {login ? 
          <SignInForm onClick={() => setlogin(false)} onSuccess={() => router.push("/applicant")}/>
        :
          <SignupForm onClick={() => setlogin(true)}/>
      }
      </div>
    </>
  );
}
