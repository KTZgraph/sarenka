interface UserCredentialsData {
  censys: {
    API_ID: string;
    Secret: string;
  };
  shodan: {
    user: string;
    api_key: string;
  };
}

export default UserCredentialsData;
