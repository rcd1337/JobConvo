import { useRouter } from 'next/router'
import styles from '@/styles/Navbar.module.css'
 
export function Navbar() {
  const router = useRouter()
  return (
    <div className={styles.navContainer}>
        <ul className={styles.nav}>
        <li><a onClick={() => router.push('/')}>Home</a></li>
        <li><a onClick={() => router.push('/applicant')}>Applications</a></li>
        <li><a onClick={() => router.push('/reports')}>Reports</a></li>
        </ul>
    </div>
  )
}