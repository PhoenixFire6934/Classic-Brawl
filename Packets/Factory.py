from Packets.Messages.Client.Login.Client_Hello_Message import ClientHelloMessage
from Packets.Messages.Client.Login.Login_Message import LoginMessage
from Packets.Messages.Client.Alliance.Alliance_Chat_Message import AllianceChatMessage
from Packets.Messages.Client.Keep_Alive_Message import KeepAliveMessage
from Packets.Messages.Client.Gameroom.Team_Create_Message import TeamCreateMessage
from Packets.Messages.Client.Battle.Go_Home_From_Offline_Practise_Message import GoHomeFromOfflinePractiseMessage
from Packets.Messages.Client.Gameroom.Team_Leave_Message import TeamLeaveMessage
from Packets.Messages.Client.Home.Ask_Profile_Message import AskProfileMessage
from Packets.Messages.Client.Alliance.Ask_For_Alliance_Data_Message import AskForAllianceDataMessage
from Packets.Messages.Client.Gameroom.Team_Set_Location_Message import TeamSetLocationMessage
from Packets.Messages.Client.Gameroom.Team_Change_Member_Settings_Message import TeamChangeMemberSettingsMessage
from Packets.Messages.Client.Analytics_Event_Message import AnalyticsEventMessage
from Packets.Messages.Client.Battle.Battle_End_Message import BattleEndMessage
from Packets.Messages.Client.Set_Name_Message import SetNameMessage
from Packets.Messages.Client.Home.Get_Leaderboard_Message import GetLeaderboardMessage
from Packets.Messages.Client.Home.Avatar_Name_Check_Request_Message import AvatarNameCheckRequestMessage
from Packets.Messages.Client.Gameroom.Team_Use_Gadget_Message import TeamUseGadgetMessage
from Packets.Messages.Client.Gameroom.Do_Not_Distrub_Message import DoNotDistrubMessage
from Packets.CommandFactory import EndClientTurn

packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10108: KeepAliveMessage,
    10110: AnalyticsEventMessage,
    10212: SetNameMessage,
    14102: EndClientTurn,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: BattleEndMessage,
    14113: AskProfileMessage,
    14403: GetLeaderboardMessage,
    14302: AskForAllianceDataMessage,
    14315: AllianceChatMessage,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14363: TeamSetLocationMessage,
    14354: TeamChangeMemberSettingsMessage,
    14372: TeamUseGadgetMessage,
    14600: AvatarNameCheckRequestMessage,
    14777: DoNotDistrubMessage,

}
