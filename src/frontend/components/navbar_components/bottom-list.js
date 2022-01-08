import Link from 'next/link';
import Image from 'next/image';
// reużywalny komponent - wazna sciezka

// TODO: podłaczyć font-awesome

const BottomList = () => {
    return (
      <ul className="bottom-list">
        {/* pierwsza opcja dolnej listy */}
        <li className="bottom-list-item">
          <Link href="/credentials">
            <a className="bottom-list-link">
                <span>5</span>
                <i className="fa fa-bell"></i>
            </a>
          </Link>
        </li>
        {/* druga opcja dolnej listy */}
        <li className="bottom-list-item">
          <Link href="/credentials">
            <a className="bottom-list-link">
                <span>7</span>
                <i className="fa fa-envelope"></i>
            </a>
          </Link>
        </li>
        {/* trzecia opcja dolnej listy */}
        <li className="bottom-list-item">
          <Link href="/credentials">
            <a className="bottom-list-link">
                <span>1</span>
                <i className="fa fa-cog"></i>
            </a>
          </Link>
        </li>
        {/* trzecia opcja dolnej listy */}
        <li className="bottom-list-item">
          <Link href="/credentials">
            <a className="bottom-list-link">
                <i className="fa fa-power-off"></i>
            </a>
          </Link>
        </li>
      </ul>
    )

}

export default BottomList;