const SearchForm = () => {
    return (
        <form className="search-form">
            <input type="text" className="search-input" placeholder="Search"/>
            {/* ważny jest typ przycisku w buttona w search */}
            <button type="button" className="search-button">
                <i className="fas fa-search"></i>
            </button>
        </form>
    )
}

export default SearchForm;