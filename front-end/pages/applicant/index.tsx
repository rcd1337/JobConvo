
import {Navbar} from "@/ui/navbar";
import {ApplicationCard} from "@/ui/application";
import styles from '@/styles/Applications.module.css'
export default function Home() {

  return (
    <>
      <Navbar/>
      <div className={styles.page}>
        <div className={styles.cardContainer}>

        <ApplicationCard />
        <ApplicationCard />
        <ApplicationCard />
        <ApplicationCard />
        </div>
      </div>
    </>
  );
}
