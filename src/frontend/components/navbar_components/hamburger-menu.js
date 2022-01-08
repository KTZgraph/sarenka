const HamburgerMenu = () => {
    const handleClick = (e) => {
        const el = e.target.parentElement;
        const elParent = el.parentElement;
        const containerElement = elParent.parentElement;
        if(containerElement.classList.contains('container')){
            containerElement.classList.toggle('change')
        }
    }


    return (
        <div className="hamburger-menu" onClick={handleClick}>
            <div className="line line-1"></div>
            <div className="line line-2"></div>
            <div className="line line-3"></div>
        </div>
    )
}

export default HamburgerMenu;