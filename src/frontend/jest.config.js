// https://github.com/vercel/next.js/blob/canary/examples/with-jest/jest.config.js
const nextJest = require('next/jest')

const createJestConfig = nextJest({dir: '.'})

// Add any custom config to be passed to Jest
const customJestConfig = {
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  moduleNameMapper: {
    // Handle module aliases (this will be automatically configured for you soon)
    '^@/components/(.*)$': '<rootDir>/components/$1',

    '^@/pages/(.*)$': '<rootDir>/pages/$1',
  },
  testEnvironment: 'jest-environment-jsdom',
  clearMocks: true, //z tutoriala https://www.youtube.com/watch?v=0DK7FX79WI0 1:12
  moduleDirectories: ['node_modules', 'src'] //z tutoriala https://www.youtube.com/watch?v=0DK7FX79WI0 1:19
}

// createJestConfig is exported this way to ensure that next/jest can load the Next.js config which is async
module.exports = createJestConfig(customJestConfig)