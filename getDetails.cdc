import Profile from 0xf41fd3cb80a5dce4
        
pub fun main(address: Address): Profile.ReadOnly? {
    return Profile.read(address)
}