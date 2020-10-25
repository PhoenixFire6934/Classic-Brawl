from Packets.Messages.Client.ClientHelloMessage import ClientHello
from Packets.Messages.Client.LoginMessage import Login
from Packets.Messages.Client.KeepAliveMessage import KeepAlive
from Packets.Messages.Client.TeamCreateMessage import CreateGameroom
from Packets.Messages.Client.GoHomeFromOfflinePractiseMessage import Exit
from Packets.Messages.Client.TeamLeaveMessage import QuitRoom
from Packets.Messages.Client.AskProfileMessage import AskProfile
from Packets.Messages.Client.AskForJoinableAlliancesListMessage import OpenClubMessage
from Packets.Messages.Client.TeamSetLocationMessage import ChangeMap
from Packets.Messages.Client.TeamChangeMemberSettingsMessage import ChangeBrawlerInRoom
from Packets.Messages.Client.AnalyticsEventMessage import AnalyticsEvent
from Packets.Messages.Client.BattleEndMessage import BattleEnd
from Packets.Messages.Client.SetNameMessage import SetName
from Packets.Messages.Client.SetContentCreatorMessage import SetContentCreator
from Packets.Messages.Client.AvatarNameCheckRequestMessage import ChangeName
from Packets.Messages.Client.TeamUseGadgetMessage import GameroomGadget
from Packets.Messages.Client.SetDoNotDistrubMessage import DoNotDistrub
from Packets.CommandFactory import EndClientTurn

packets = {
    10100: ClientHello,
    10101: Login,
    10108: KeepAlive,
    10110: AnalyticsEvent,
    18686: SetContentCreator,
    10212: SetName,
    14102: EndClientTurn,
    14109: Exit,
    14110: BattleEnd,
    14113: AskProfile,
    14303: OpenClubMessage,
    14350: CreateGameroom,
    14353: QuitRoom,
    14363: ChangeMap,
    14354: ChangeBrawlerInRoom,
    14372: GameroomGadget,
    14600: ChangeName,
    14777: DoNotDistrub
}
