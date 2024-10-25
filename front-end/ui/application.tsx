import { signin } from '@/actions/auth'
import styles from '@/styles/Applications.module.css'
 
export function ApplicationCard({onApplyClick, onDeleteClick, onEditClick, isCompany}) {
  return (
    <div className={styles.card}>
        <p>Empresa: Mock</p>
        <p>Base salarial: Mock</p>
        <p>Requisitos: Mock</p>
        <p>Escolaridade: Mock</p>
        {isCompany ? 
            <div>
                <button>Editar</button>
                <button>Deletar</button>    
            </div>
        : 
            <button>Candidatar</button>
        }
        
    </div>
  )
}