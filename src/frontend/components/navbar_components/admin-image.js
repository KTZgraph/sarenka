import Image from 'next/image';

const AdminImage = () => {
    return (
        <div className="card">
            {/* obbrazek admina */}
            <div className="card-img">
                <Image src="/logo.png" className="admin-image" alt="Admin Image" width={135} height={150}/>
            </div>
            <div className="card-body">
                <h2 className="card-title">SARENKA</h2>
                <p className="card-subtitle">Administrator</p>
            </div>    
        </div>
    )
}

export default AdminImage;