import Image from "next/image";
import Link from "next/link";

import classes from "./app-image.module.css";

function AppImage(props) {
  return (
    <Link href="/">
      <a className={classes.logo}>
        <div className={classes.card}>
          <div className={classes.cardImg}>
            <Image
              src="/logo.png"
              className="admin-image"
              alt="Admin Image"
              width={40}
              height={40}
            />
          </div>
          <div className={classes.cardBody}>
            <h2 className="card-title">SARENKA</h2>
            {/* warunkowo jak user zalogowany */}
            {props.userEmail && (
              <p className="card-subtitle">{props.userEmail}</p>
            )}
          </div>
        </div>
      </a>
    </Link>
  );
}

export default AppImage;