-- Table: MavenRepository
CREATE TABLE MavenRepository (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url TEXT NOT NULL,
    lastRefreshed DATE,
    state INT DEFAULT 0, -- 0 = unvisited, 1 = visited, 2 = error
    stateMsg TEXT
);

-- Table: MavenArtifact
CREATE TABLE MavenArtifact (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    groupId VARCHAR(255) NOT NULL,
    mavenRepositoryId INT REFERENCES MavenRepository(id) ON DELETE CASCADE,
    lastRefreshed DATE DEFAULT NULL,
    state INT DEFAULT 0, -- 0 = unvisited, 1 = visited, 2 = error
    stateMsg TEXT,
    githubUrl TEXT,
    githubConnection TEXT,
    latestVersion VARCHAR(50),
    latestVersionPomUrl TEXT,
    latestVersionPomProcessedDate DATE DEFAULT NULL
);
