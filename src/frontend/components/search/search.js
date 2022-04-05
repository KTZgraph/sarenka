import SearchForm from "./search-form";
import classes from "./search.module.css";

function Search() {
  return (
    <>
      <div className={classes.search}>
        <div className={classes.searchItems}>
          <SearchForm />
          {/* searchdata */}
        </div>
      </div>
    </>
  );
}

export default Search;
