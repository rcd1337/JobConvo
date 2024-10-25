import { signin } from '@/actions/auth'
import { useRouter } from 'next/router'
import styles from '@/styles/Forms.module.css'
 
export function SignInForm({onClick}) {
  const router = useRouter()
  return (
    <form action={signin} className={styles.fields}>
      <div>
        <label htmlFor="email">Email</label>
        <input id="email" name="email" type="email" placeholder="Email" />
      </div>
      <div>
        <label htmlFor="password">Password</label>
        <input id="password" name="password" type="password" />
      </div>
      <div className={styles.buttons}>
        <button className={styles.button} type="submit" onClick={() => router.push('/')}>Sign In</button>
        <button className={styles.button} type="button" onClick={onClick}>Sign Up</button>
      </div>
    </form>
  )
}