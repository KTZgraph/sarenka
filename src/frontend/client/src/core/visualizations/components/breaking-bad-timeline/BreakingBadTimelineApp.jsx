import { useEffect, useState } from 'react';
import BreakingBadTimeline from './BreakingBadTimeline';

const BreakingBadTimelineApp = () => {
  const [bbEpisodes, setBbEpisodes] = useState([]);
  const [bbCharacters, setBbCharacters] = useState([]);
  const [highlight, setHighlight] = useState();

  useEffect(() => {
    fetch(
      'https://www.breakingbadapi.com/api/characters?category=Breaking+Bad'
    )
      .then((response) => response.ok && response.json())
      .then((characters) => {
        setBbCharacters(
          characters.sort((a, b) => a.name.localeCompare(b.name))
        );
      })
      .catch(console.error);
  }, []);

  useEffect(() => {
    fetch(
      'https://www.breakingbadapi.com/api/episodes?series=Breaking+Bad'
    )
      .then((response) => response.ok && response.json())
      .then((episodes) => {
        console.warn(episodes);
        setBbEpisodes(episodes);
      })
      .catch(console.error);
  }, []);

  if (bbEpisodes)
    return (
      <div
        style={{ width: '100%', height: '100%', overflow: 'visible' }}
      >
        <h1>Breaking Bad timeline</h1>
        <BreakingBadTimeline highligh={highlight} data={bbEpisodes} />
        <select
          value={highlight}
          onChange={(e) => setHighlight(e.target.value)}
        >
          <option>Select character</option>
          {bbCharacters.map((character) => (
            <option key={character.name}>{character.name}</option>
          ))}
        </select>
      </div>
    );
};

export default BreakingBadTimelineApp;
