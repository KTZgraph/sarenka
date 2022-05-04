
import { render, screen } from '@testing-library/react'
import SearchPage from '@/pages/index'

test('renders learn eack link', () => {
    render(<SearchPage/>);
    const linkElement = screen.getByText(/sarenka*/i);
    expect(linkElement).toBeInTheDocument();
})