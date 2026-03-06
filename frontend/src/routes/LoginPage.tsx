import { API_URL } from '../config';
import styles from '../styles/LoginPage.module.css';

export function LoginPage() {
  const handleLogin = () => {
    window.location.href = `${API_URL}/login`;
  };

  return (
    <div className={styles.page}>
      <div className={styles.card}>
        <h1 className={styles.title}>My Home Server</h1>
        <p className={styles.subtitle}>Авторизация через Google</p>
        <button type="button" className={styles.button} onClick={handleLogin}>
          Войти через Google
        </button>
      </div>
    </div>
  );
}

