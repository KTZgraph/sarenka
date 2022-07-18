import styles from "./Comment.module.scss";

const Comment = () => {
  return (
    <div className={styles.form}>
      <div className={styles.formContainer}>
        <div className={styles.left}>
          <textarea></textarea>
          <div className={styles.submit}>Sumbit</div>
        </div>
        <div className={styles.rignt}>radiobutton</div>
      </div>
    </div>
  );
};

export default Comment;
