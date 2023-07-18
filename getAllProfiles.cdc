import Library from 0xf41fd3cb80a5dce4

pub fun main(): [{Address: Library.Profile}] {
    return Library.getAllProfiles()
}