import postgres from 'postgres'

export function Page(Marble) {
  const sql = postgres({
    host: process.env.DATABASE_HOST,
    database: process.env.DATABASE_NAME,
    username: process.env.DATABASE_USER,
    password: process.env.DATABASE_PASSWORD,
    ssl: 'require',
  })

  return <>...</>
}
